import langchain
from langchain.llms.base import LLM, Optional, List, Mapping, Any
import requests
from pydantic import Field

def fix_code_block(text):
    text = text.replace("'''", "```")

    segments = text.split('`')
    for i in range(len(segments)):
        if i % 2 == 1:  # If the segment is within a pair of backticks
            segments[i] = segments[i].replace("'", "`")

    return '`'.join(segments)

class KoboldApiLLM(LLM):
    endpoint: str = Field(...)
    
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]]=None) -> str:
        # Prepare the JSON data
        data = {
            "prompt": prompt,
            "use_story": False,
            "use_authors_note": False,
            "use_world_info": False,
            "use_memory": False,
            "max_context_length": 1600,
            "max_length": 1800,
            "rep_pen": 1.12,
            "rep_pen_range": 1024,
            "rep_pen_slope": 0.9,
            "temperature": 0.6,
            "tfs": 0.9,
            "top_p": 0.95,
            "top_k": 0.6,
            "typical": 1,
            "frmttriminc": True
        }

        # Add the stop sequences to the data if they are provided
        if stop is not None:
            data["stop_sequence"] = stop

        # Send a POST request to the Kobold API with the data
        response = requests.post(f"{self.endpoint}/api/v1/generate", json=data)

        # Check for the expected keys in the response JSON
        json_response = response.json()
        if "results" in json_response and len(json_response["results"]) > 0 and "text" in json_response["results"][0]:
            # Return the generated text
            text = json_response["results"][0]["text"].strip()

            # Remove the stop sequence from the end of the text, if it's there
            if stop is not None:
                for sequence in stop:
                    if text.endswith(sequence):
                        text = text[: -len(sequence)].rstrip()


            fixed_text = fix_code_block(text)
            print(fixed_text)
            return fix_code_block(fixed_text)
        else:
            raise ValueError("Unexpected response format from Kobold API")


    
    def __call__(self, prompt: str, stop: Optional[List[str]]=None) -> str:
        return self._call(prompt, stop)

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {'endpoint': self.endpoint} #return the kobold_ai_api as an identifying parameter
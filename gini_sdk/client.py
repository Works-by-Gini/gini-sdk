import requests
import json
from typing import Dict, Any, List
from .crypto.encryption import Encryptor
from .models import Attachment

class GiniClient:
    def __init__(self, api_key: str, port: int, host: str = "localhost"):
        """Initialize the Gini SDK client.
        
        Args:
            api_key: The API key for authentication
            host: The host address of the server
            port: The port number of the server
        """
        self.api_key = api_key
        self.base_url = f"http://{host}:{port}"
        self.encryptor = Encryptor(api_key)

    def execute_gini(self, gini_id: str, input : str, attachments: List[Attachment]) -> Dict[str, Any]:
        """Execute a Gini request.
        
        Args:
            gini_id: The ID of the Gini to execute
            input: The input to the Gini
            
        Returns:
            Dict containing the response from Gini
            
        Raises:
            RequestError: If the request fails
            ConnectionError: If unable to connect to the server
        """
        request_data = {
            "action": "EXECUTE_GINI",
            "data": {
                "giniID": gini_id,
                "value": input,
                "attachments": []
            }
        }
        
        # Encrypt the request
        encrypted_payload = self.encryptor.encrypt_message(json.dumps(request_data))
        
        # Send request to server
        try:
            response = requests.post(
                f"{self.base_url}/execute",
                json={"payload": encrypted_payload},
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            
            # Decrypt and return the response
            encrypted_response = response.json()["payload"]
            decrypted_response = self.encryptor.decrypt_message(encrypted_response)
            return json.loads(decrypted_response)
            
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to server: {str(e)}")
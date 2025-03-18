# Secret Vault App

This is a simple Flask-based vault-like application that allows users to store secrets in an encrypted format. The app provides endpoints to update and retrieve secrets. The secrets are stored in an encrypted file, and only the authorized user can decrypt them.

## Features

- **Store Secrets**: Save secrets in an encrypted format.
- **Retrieve Secrets**: Decrypt and retrieve stored secrets.
- **Encryption**: Use AES-256-CBC encryption to store secrets securely.

## Prerequisites

Before running the app, ensure that you have the following installed:

- Python 3.x
- Flask
- OpenSSL (for encryption/decryption)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/secret-vault.git
   cd secret-vault
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## Usage
### 1. Start the Flask App:

To run the Flask app locally, use the following command:
```bash
python app.py
```
### 2. Update a Secret:

You can update a secret in the encrypted file using the PUT request. Use the following curl command to update a secret:

```bash
curl -X PUT "http://127.0.0.1:5000/update?file_path=data-encript" \
     -H "Content-Type: application/json" \
     -d '{"gender": "male"}'
```
- **file_path:** The path to the encrypted file where the secret is stored.
- **data:** The JSON data that contains the secret you want to store (e.g., {"gender": "male"}).

### 3. Retrieve a Secret:

To retrieve a secret from the encrypted file, use the GET request. The following curl command decrypts and retrieves the secret:

```bash
curl -X GET "http://127.0.0.1:5000/secret?file_name=data-encript&token=asdf123a"
```
- **file_name:** The name of the encrypted file you want to retrieve the secret from.
- **token:** The decryption token (password) used to decrypt the file.

### 4. Error Handling:

If a file does not exist or there are issues with decryption, the app will return an error message.
Ensure the file_name and token match the encrypted file and its decryption key.

## Security
- **Encryption:** This app uses AES-256-CBC encryption to securely store secrets.
- **Decryption Token:** To retrieve the secrets, you need the correct decryption token (token parameter in the GET request).
  
**Important:** Ensure the decryption token is kept secure, as it is required to access the secrets.

import hvac

# Configure o cliente do Vault
vault_url = "http://<VAULT_SERVER>:8200"  # Substitua pelo endereço do Vault
vault_token = "<VAULT_TOKEN>"  # Token gerado no Vault
client = hvac.Client(url=vault_url, token=vault_token)

# Verifique se está autenticado
if not client.is_authenticated():
    raise Exception("Failed to authenticate with Vault!")

# Acesse os segredos
secret_path = "secret/data/aws"
response = client.secrets.kv.read_secret_version(path=secret_path)
credentials = response['data']['data']

glue_user = credentials['glue-user']
glue_password = credentials['glue-password']

print(f"Glue User: {glue_user}")
print(f"Glue Password: {glue_password}")

import json
from pyatlan.client.atlan import AtlanClient
from pyatlan.model.lineage import LineageRequest
from pyatlan.model.core import EntityReference

# Configuração do cliente Atlan
client = AtlanClient(base_url="https://seu-dominio.atlan.com", api_key="SUA_CHAVE_DE_API")

# Carregar JSON com os dados da linhagem
with open("linhagem.json", "r") as f:
    data = json.load(f)

# Extraindo informações do JSON
job_name = data["job"]["name"]
namespace = data["job"]["namespace"]

# Criando lista de relações de linhagem
for input_data in data["inputs"]:
    for output_data in data["outputs"]:
        origem = EntityReference(type_name="Table", qualified_name=f"{namespace}/{input_data['name']}")
        destino = EntityReference(type_name="Table", qualified_name=f"{namespace}/{output_data['name']}")

        linha = LineageRequest(
            from_entity=origem,
            to_entity=destino,
            process_qualified_name=f"{namespace}/{job_name}"  # Nome do processo ETL
        )

        # Enviar a relação de linhagem para o Atlan
        client.lineage.create(linha)

print("Linhagem enviada com sucesso!")

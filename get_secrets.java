import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.secretsmanager.SecretsManagerClient;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueRequest;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueResponse;
import software.amazon.awssdk.services.secretsmanager.model.SecretsManagerException;

public class SecretsManagerExample {

    public static void main(String[] args) {
        String secretName = "seu-segredo";
        Region region = Region.US_EAST_1; // Especifique a região do seu segredo

        // Cria um cliente do Secrets Manager
        try (SecretsManagerClient secretsClient = SecretsManagerClient.builder()
                .region(region)
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build()) {

            // Recupera o valor do segredo
            String secretValue = getSecretValue(secretsClient, secretName);
            System.out.println("Valor do segredo: " + secretValue);
        }
    }

    public static String getSecretValue(SecretsManagerClient client, String secretName) {
        try {
            GetSecretValueRequest valueRequest = GetSecretValueRequest.builder()
                    .secretId(secretName)
                    .build();

            GetSecretValueResponse valueResponse = client.getSecretValue(valueRequest);
            return valueResponse.secretString();
        } catch (SecretsManagerException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            throw e;
        }
    }
}

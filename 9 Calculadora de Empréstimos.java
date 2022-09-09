import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final byte MESES_DO_ANO = 12;
        final byte PORCENTAGEM = 100;

        System.out.println("\nCalculadora de Empréstimo");
        System.out.println("Desenvolvida como projeto para programação em Java.\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Valor total desejado:");
        int valorTotal = scanner.nextInt();

        System.out.print("Juros anuais:");
        float jurosAnuais = scanner.nextFloat();
        float jurosMensais = (jurosAnuais/PORCENTAGEM)/MESES_DO_ANO;

        System.out.print("Em quantos anos pretende pagar:");
        byte anos = scanner.nextByte();
        int numeroDePagamentos = anos * MESES_DO_ANO;

        double valorMensal = valorTotal
                * (jurosMensais * Math.pow(1 + jurosMensais, numeroDePagamentos))
                / (Math.pow(1 + jurosMensais, numeroDePagamentos) - 1);

        String valorMensalFormatado = NumberFormat.getCurrencyInstance().format(valorMensal);
        System.out.println("Parcelas mensais no valor de: " + valorMensalFormatado);

        int totalPago = (int)valorMensal * numeroDePagamentos;
        String totalFormatado = NumberFormat.getCurrencyInstance().format(totalPago);
        System.out.println("\nO valor total a ser pago é de:" + totalFormatado);

        int valorDosJuros = totalPago - valorTotal;
        String valorJurosFormatado = NumberFormat.getCurrencyInstance().format(valorDosJuros);
        System.out.println("Total de juros: " + valorJurosFormatado);

        }
    }

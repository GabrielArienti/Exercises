import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    final static byte MESES_DO_ANO = 12;
    final static byte PORCENTAGEM = 100;

    public static void main(String[] args) {
        double totalPago ;

        System.out.println("\nCalculadora de Empréstimo");
        System.out.println("Desenvolvida como projeto para programação em Java.\n");

        int valorTotal = (int) lerValor("Valor total desejado, entre R$1 mil e R$1 milhão: ", 1000, 1000000);
        float jurosAnuais = (float) lerValor("Digite os juros anuais: ", 1, 100);
        byte anos = (byte) lerValor("Em quantos anos pretende pagar: ", 1, 50);

        double valorMensal = calcularFinanciamento(valorTotal, jurosAnuais, anos);
        String valorMensalFormatado = NumberFormat.getCurrencyInstance().format(valorMensal);
        System.out.println("Parcelas mensais no valor de: " + valorMensalFormatado);

        totalPago = totalPago(anos, valorMensal);
        totalDeJuros(totalPago, valorTotal);
        exibirParcelas(valorTotal, jurosAnuais, anos);
    }

    private static void exibirParcelas(int valorTotal, float jurosAnuais, byte anos) {
        System.out.println();
        System.out.println("--------------");
        System.out.println("Agenda de Pagamentos Mensais:");
        System.out.println("--------------");
        for (short meses = 1; meses <= anos * MESES_DO_ANO; meses++) {
            double balanco = calcularPagamentos(valorTotal, jurosAnuais, anos, meses);
            System.out.println(meses + "- " + NumberFormat.getCurrencyInstance().format(balanco));
        }
    }

    private static double totalPago(byte anos, double valorMensal) {
        double totalPago;
        totalPago = (valorMensal * (anos * MESES_DO_ANO));
        String totalFormatado = NumberFormat.getCurrencyInstance().format(totalPago);
        System.out.println("\nO valor total a ser pago é de:" + totalFormatado);
        return totalPago;
    }

    private static void totalDeJuros(double totalPago, int valorTotal) {
        int valorDosJuros = (int)(totalPago - valorTotal);
        String valorJurosFormatado = NumberFormat.getCurrencyInstance().format(valorDosJuros);
        System.out.println("Total de juros: " + valorJurosFormatado);
    }

    public static double lerValor(String promt, double min, double max){
        Scanner scanner = new Scanner (System.in);
        double valor;
        while (true) {
            System.out.print(promt);
            valor = scanner.nextInt();
            if (valor >= min && valor <= max)
                break;
            System.out.println("Digite um valor entre " + " " + min + "e " + " " + max);
        }
        return valor;
    }

    public static double calcularPagamentos(int valorTotal, float jurosAnuais, byte anos, short numeroDeParcelasPagas){

        float jurosMensais = (jurosAnuais / PORCENTAGEM) / MESES_DO_ANO;
        short numeroDePagamentos = (short)(anos * MESES_DO_ANO);

        double balanco = valorTotal
                * (Math.pow(1 + jurosMensais, numeroDePagamentos) - Math.pow(1 + jurosMensais, numeroDeParcelasPagas))
                / (Math.pow(1 + jurosMensais, numeroDePagamentos) - 1);

        return balanco;
    }
    public static double calcularFinanciamento (int valorTotal, float jurosAnuais, byte anos) {

        float jurosMensais = (jurosAnuais / PORCENTAGEM) / MESES_DO_ANO;
        short numeroDePagamentos = (short)(anos * MESES_DO_ANO);

        double valorMensal = valorTotal
                * (jurosMensais * Math.pow(1 + jurosMensais, numeroDePagamentos))
                / (Math.pow(1 + jurosMensais, numeroDePagamentos) - 1);

        return valorMensal;
    }
}

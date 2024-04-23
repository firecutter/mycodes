<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processamento do Formulário</title>
</head>
<body>
    <h2>Dados Recebidos do Formulário</h2>
    <?php
    // Verifica se os campos foram preenchidos
    if(isset($_POST['nome'], $_POST['departamento'], $_POST['cargo'])) {
        // Captura os dados do formulário
        $nome = $_POST['nome'];
        $departamento = $_POST['departamento'];
        $cargo = $_POST['cargo'];

        // Exibe os dados capturados
        echo "<p>Nome: $nome</p>";
        echo "<p>Departamento: $departamento</p>";
        echo "<p>Cargo: $cargo</p>";

        // Contagem dos cargos
        $cargos = [];
        if(file_exists('dados.txt')) {
            $conteudo = file_get_contents('dados.txt');
            $cargos = unserialize($conteudo);
        }
        if(array_key_exists($cargo, $cargos)) {
            $cargos[$cargo]++;
        } else {
            $cargos[$cargo] = 1;
        }
        file_put_contents('dados.txt', serialize($cargos));
    } else {
        echo "<p>Por favor, preencha todos os campos do formulário.</p>";
    }
    ?>
    <h2>Gráfico de Cargos</h2>
    <table border="1">
        <tr>
            <th>Cargo</th>
            <th>Número de Pessoas</th>
        </tr>
        <?php
        // Exibindo o gráfico
        if(isset($cargos) && !empty($cargos)) {
            foreach($cargos as $cargo => $quantidade) {
                echo "<tr>";
                echo "<td>$cargo</td>";
                echo "<td>$quantidade</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='2'>Nenhum dado disponível.</td></tr>";
        }
        ?>
    </table>
</body>
</html>
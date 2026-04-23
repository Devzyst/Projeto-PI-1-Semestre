# Informações 
## Tecnologias Ultilizadas: 
IDE para desenvolvimento: VSCode <br>
Linguagem de programação: Python <br>
Banco de Dados: MySQL <br>
Repositório: Git com Github <br>
Gerenciamento do projeto: Github Project.

## Descrição Do Projeto
 Este projeto consiste no desenvolvimento de um sistema de votação digital, criado como atividade acadêmica,
seguindo as diretrizes estabelecidas pelo professor da disciplina.
 A aplicação foi desenvolvida utilizando a linguagem Python, com integração a banco de dados MySQL, e versionamento de código através de Git e GitHub,
utilizando o ambiente de desenvolvimento Visual Studio Code.
 O sistema possui duas funcionalidades principais: gerenciamento de usuários e votação.
 Ao iniciar a aplicação, o usuário pode escolher entre acessar a área de gerenciamento, onde é possível visualizar e editar informações da conta,
ou acessar a área de votação, onde pode participar do processo de votação de forma simples e segura.
 Um dos diferenciais do projeto é a implementação de criptografia do CPF utilizando a Cifra de Hill,
garantindo maior segurança no armazenamento e manipulação de dados sensíveis. Além disso, o sistema conta com integração completa com banco de dados,
permitindo persistência e organização eficiente das informações.
 O projeto foi desenvolvido em grupo, contando com a colaboração de cinco integrantes,
promovendo a divisão de tarefas e o uso de boas práticas de desenvolvimento em equipe.

## Instruções para execução do sistema
 O sistema de votação digital deve ser utilizado a partir da execução da aplicação, que apresenta ao usuário as opções de acesso ao gerenciamento e à votação. <br>
* Ao iniciar o sistema, o usuário deve escolher a funcionalidade desejada. A opção de gerenciamento é destinada à administração dos dados, enquanto a opção de votação é utilizada para registrar votos. <br>
* Ao acessar o gerenciamento, o usuário pode visualizar os dados cadastrados no sistema, incluindo informações de eleitores e candidatos. É possível editar dados de eleitores, como nome, CPF e título de eleitor, além de redefinir senhas quando necessário. <br>
* Ainda no gerenciamento, o usuário pode cadastrar novos candidatos, informando nome, partido e número de urna. O sistema realiza verificações para evitar duplicidade de informações. Também é possível editar ou remover candidatos já cadastrados <br>
* O gerenciamento também permite a visualização geral dos registros armazenados no banco de dados, garantindo o controle e a organização das informações, além de possibilitar a verificação de permissões de acesso conforme o tipo de usuário. <br>
* Ao selecionar a opção de votação, o sistema solicita a identificação do eleitor. Para isso, é necessário informar o título de eleitor, parte do CPF e a chave de acesso. <br>
* Após o preenchimento, o sistema realiza a validação dos dados, confirmando se o eleitor está cadastrado e se ainda não realizou seu voto. <br>
* Caso o eleitor esteja apto, o sistema libera a etapa de votação, onde deve ser informado o número do candidato desejado. Em seguida, são exibidas as informações do candidato para conferência. <br>
* O usuário deve confirmar o voto para que ele seja registrado. Caso haja algum erro, é possível corrigir antes da confirmação final. <br>
* Após a confirmação, o voto é armazenado no banco de dados, um protocolo é gerado como comprovante e o sistema atualiza o status do eleitor, impedindo que ele vote novamente. <br>
* O sistema também possui a funcionalidade de encerramento da votação, que deve ser realizada por um usuário autorizado. Após a validação das credenciais, o processo é finalizado. <br>
* Com a votação encerrada, o sistema disponibiliza os resultados, incluindo a contagem de votos por candidato e outras informações estatísticas, além de manter registros de auditoria, como logs de acesso e operações realizadas, garantindo a integridade e a confiabilidade do processo. <br>

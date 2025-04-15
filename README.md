Este é um script em Python que coleta informações de um aluno e suas notas, calcula a média final e gera automaticamente um boletim escolar em formato PDF.

🚀 Funcionalidades
Coleta de dados do aluno (nome, escola, curso, número da sala e matrícula);

Entrada de 12 notas num intervalo de 0 a 10;

Cálculo automático da média final;

Geração de um boletim formatado em PDF;

Instalação automática do módulo fpdf caso não esteja instalado.

🧰 Requisitos
Python 3.x

A biblioteca fpdf (será instalada automaticamente se não estiver presente)

📥 Instalação
Clone o repositório ou apenas baixe o arquivo .py.

Não é necessário instalar manualmente o fpdf, pois o próprio script se encarrega disso na primeira execução.

bash
Copiar
Editar
git clone https://github.com/seu-usuario/boletim-escolar.git
cd boletim-escolar
▶️ Como Executar
Basta rodar o script no terminal:

bash
Copiar
Editar
python boletim_escolar.py
Você será guiado por um processo interativo no terminal para inserir as informações necessárias. Após isso, um boletim em PDF será gerado automaticamente no mesmo diretório do script.

📄 Exemplo de Saída
Um arquivo PDF será criado com o nome:

Copiar
Editar
boletim_NOME_DO_ALUNO.pdf
E incluirá:

Informações do aluno;

Lista das 12 notas;

Média final calculada e exibida centralizadamente.

📌 Observações
Certifique-se de inserir notas válidas (entre 0 e 10);

O nome do arquivo PDF será baseado no nome do aluno, com espaços substituídos por underscores (_);

O script é auto-suficiente, ideal para uso em ambientes educacionais simples ou como projeto acadêmico.

📚 Licença
Este projeto é de uso livre para fins educacionais.

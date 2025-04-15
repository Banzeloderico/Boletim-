try:
    from fpdf import FPDF
except ModuleNotFoundError:
    print("O módulo 'fpdf' não está instalado. Instalando automaticamente...")
    import os
    os.system("pip install fpdf")
    from fpdf import FPDF

def coletar_informacoes():
    print("Bem-vindo ao sistema de Boletim Escolar\n")
    
    # Coleta de informações do aluno
    nome = input("Digite o nome do aluno: ")
    numero_sala = input("Digite o número da sala: ")
    nome_escola = input("Digite o nome da escola: ")
    curso = input("Digite o nome do curso: ")
    numero_aluno = input("Digite o número do aluno: ")

    # Coleta de 12 notas
    print("\nInsira as notas do trimestre:")
    notas = []
    for i in range(1, 13):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota (entre 0 e 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    # Calcula a média
    media = sum(notas) / len(notas)
    
    return {
        "nome": nome,
        "numero_sala": numero_sala,
        "nome_escola": nome_escola,
        "curso": curso,
        "numero_aluno": numero_aluno,
        "notas": notas,
        "media": media
    }

def gerar_boletim(dados_aluno):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Cabeçalho
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Boletim Escolar", ln=True, align="C")
    pdf.ln(10)
    
    # Informações do aluno
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Nome do aluno: {dados_aluno['nome']}", ln=True)
    pdf.cell(200, 10, txt=f"Número da sala: {dados_aluno['numero_sala']}", ln=True)
    pdf.cell(200, 10, txt=f"Escola: {dados_aluno['nome_escola']}", ln=True)
    pdf.cell(200, 10, txt=f"Curso: {dados_aluno['curso']}", ln=True)
    pdf.cell(200, 10, txt=f"Número do aluno: {dados_aluno['numero_aluno']}", ln=True)
    pdf.ln(10)
    
    # Notas
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Notas do Trimestre", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    for i, nota in enumerate(dados_aluno['notas'], start=1):
        pdf.cell(200, 10, txt=f"{i}ª Nota: {nota:.2f}", ln=True)
    pdf.ln(5)
    
    # Média final
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt=f"Média Final: {dados_aluno['media']:.2f}", ln=True, align="C")
    
    # Salva o PDF
    nome_arquivo = f"boletim_{dados_aluno['nome'].replace(' ', '_')}.pdf"
    pdf.output(nome_arquivo)
    print(f"\nBoletim gerado com sucesso! Arquivo salvo como: {nome_arquivo}")

if __name__ == "__main__":
    dados_aluno = coletar_informacoes()
    gerar_boletim(dados_aluno)

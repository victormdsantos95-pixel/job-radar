import os
from dotenv import load_dotenv

load_dotenv()

# Cargo forte: título que já indica diretamente uma vaga do perfil de
# suporte técnico, customer success, CX ou legal tech / Espaider.
KEYWORDS_CARGO_FORTE = [
    "Analista de Suporte",
    "Suporte Técnico",
    "Suporte N2",
    "Suporte N3",
    "Analista de Suporte N2",
    "Analista de Suporte N3",
    "Application Support",
    "Analista de Implantação",
    "Consultor de Implantação",
    "Analista de Customer Success",
    "Customer Success Analyst",
    "CS Analyst",
    "Analista de CX",
    "CX Analyst",
    "Customer Experience Analyst",
    "Analista de Service Desk",
    "Service Desk Analyst",
    "Analista de Help Desk",
    "Help Desk Sênior",
    "Legal Tech",
    "Consultor Legal Tech",
    "Analista Espaider",
    "Consultor de Software Jurídico",
]

# Cargo ambíguo: título que também é usado em vaga sem nada a ver com o
# perfil (ex: "Business Analyst" e "Analyst" existem em qualquer área). Só
# conta como match se o título TAMBÉM tiver um QUALIFICADORES_DADOS junto.
KEYWORDS_CARGO_AMBIGUO = [
    "Business Analyst",
    "Analista de Negócios",
    "Analista de Sistemas Jurídicos",
    "Analyst",
]

# Termo que precisa aparecer junto no título quando o cargo é ambíguo, pra
# confirmar que é vaga do perfil de suporte, CS/CX ou legal tech, e não de
# outra área qualquer.
QUALIFICADORES_DADOS = [
    "suporte",
    "support",
    "cliente",
    "customer",
    "sistemas",
    "software",
    "jurídico",
    "erp",
    "sql",
    "sla",
    "atendimento",
]

# Ferramenta que aparece como núcleo do título. Só conta como match se o
# título TAMBÉM tiver uma palavra de cargo — evita pegar vaga de
# desenvolvimento da ferramenta, que não é o perfil buscado.
FERRAMENTAS_TITULO = [
    "Espaider",
    "Movidesk",
]

# Palavra de cargo que confirma que a vaga de ferramenta é de suporte ou
# consultoria, não de desenvolvimento.
QUALIFICADORES_CARGO = [
    "analista",
    "analyst",
    "especialista",
    "specialist",
    "consultor",
    "consultant",
]

KEYWORDS = KEYWORDS_CARGO_FORTE + KEYWORDS_CARGO_AMBIGUO

# Termos de busca enviados a cada site. TERMOS_CARGO é derivado direto de
# KEYWORDS, assim toda keyword nova em KEYWORDS já vira busca também, sem
# precisar manter duas listas em sincronia à mão.
TERMOS_CARGO_EXTRA = [
    "help desk",
    "atendimento ao cliente",
]

TERMOS_CARGO = sorted(set(k.lower() for k in KEYWORDS) | set(TERMOS_CARGO_EXTRA))

TERMOS_FERRAMENTA = [
    "espaider",
    "movidesk",
    "sql",
]

TERMOS_BUSCA = TERMOS_CARGO + TERMOS_FERRAMENTA

# Termos que rodam em TODO ciclo, fora do rodízio, por serem os títulos
# que mais interessam no perfil buscado.
TERMOS_PRIORITARIOS = [
    "analista de suporte",
    "suporte técnico",
    "customer success",
    "analista de cx",
    "business analyst",
]

TERMOS_POR_CICLO = 10

# Onde vaga HIBRIDA ou PRESENCIAL e aceita (mais "Remoto", que nao e
# cidade e sim a porta de entrada da regra de modalidade remota — ver
# _FLAGS_REMOTO em job.py). Vaga hibrida/presencial fora desta lista e
# rejeitada; e uma whitelist, nao uma preferencia de ordenacao.
#
# Só Blumenau, onde o usuário mora, e Remoto.
CIDADES = [
    "Remoto",
    "Blumenau",
]

CIDADES_EUROPA_IBERICA = [
    "Portugal",
    "Lisboa",
    "Porto",
    "Braga",
    "Espanha",
    "España",
    "Spain",
    "Madrid",
    "Barcelona",
    "Valencia",
]

ATIVAR_EIXO_IBERICO_BR = False

LOCATIONS_LINKEDIN = ["Brazil"]

LOCATIONS_LINKEDIN_REMOTO_APENAS = ["Argentina", "Chile", "Mexico", "Colombia", "Espanha", "Portugal"]

LOCATIONS_LINKEDIN_CIDADES_PRESENCIAL = [c for c in CIDADES if c != "Remoto"]

MERCADOS_REMOTO_ACEITOS = ["Brasil", "LATAM", "Argentina", "Chile", "México", "Colômbia", "Portugal", "Espanha"]

INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 180))

# Vaga com Job.pontuar_relevancia() >= este limiar notifica na hora; abaixo
# disso, fica na fila do digest diário.
LIMIAR_DIGEST_IMEDIATO = 7

# Hora UTC a partir da qual o digest diário pode sair.
DIGEST_HORA_UTC = 9

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Caminho ancorado na RAIZ do projeto, não na pasta deste arquivo.
_RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.getenv("JOBRADAR_DB_PATH") or os.path.join(_RAIZ_PROJETO, "data", "jobs.db")

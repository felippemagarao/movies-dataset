import streamlit as st

# Configuração da página deve ser a primeira linha
st.set_page_config(page_title="MotionTech Solutions", layout="wide")

# Definição das páginas
def main_page():
    st.title("📌 MotionTech Solutions - Plano Estratégico")
    st.markdown("### 🌐 Navegação entre páginas")
    st.markdown("[🏢 Cenário da Empresa](#cenário-da-empresa)")
    st.markdown("[🎯 Objetivos Estratégicos](#objetivos-estratégicos)")
    st.markdown("[📊 Iniciativas, KPIs e Metas SMART](#iniciativas-kpis-metas)")
    st.markdown("[💻 Papel da TI como Vantagem Competitiva](#papel-da-ti)")
    st.markdown("[📈 Balanced Scorecard](#balanced-scorecard)")
    st.markdown("#### 🔄 [Retornar ao Topo](#topo)")

def page1():
    st.title("🏢 Cenário da Empresa")
    st.markdown("""
    **Nome:** MotionTech Solutions  
    **Missão:** Oferecer soluções tecnológicas inovadoras que transformem negócios por meio da automação inteligente.  
    **Visão:** Ser referência na América Latina como principal empresa de tecnologia para automação inteligente até 2030.  
    **Valores:**  
    - Inovação contínua  
    - Foco no cliente  
    - Ética e transparência  
    - Colaboração  
    - Excelência operacional  
    """)
    st.markdown("🔄 [Retornar ao Topo](#topo) | 🔙 [Página Principal](#motiontech-solutions)")

def page2():
    st.title("🎯 Objetivos Estratégicos por Perspectiva (Balanced Scorecard)")
    st.markdown("""
    **Perspectiva** | **Objetivos Estratégicos**  
    --- | ---  
    Financeira | Aumentar a receita recorrente; reduzir custos operacionais  
    Clientes | Aumentar satisfação e retenção; ampliar base de clientes B2B  
    Processos Internos | Otimizar processos de desenvolvimento e entrega; garantir alta qualidade  
    Aprendizado e Inovação | Fomentar inovação; desenvolver competências técnicas na equipe  
    """)
    st.markdown("🔄 [Retornar ao Topo](#topo) | 🔙 [Página Principal](#motiontech-solutions)")

def page3():
    st.title("📊 Iniciativas, KPIs e Metas SMART")
    st.markdown("""
    **Objetivo** | **Iniciativa Estratégica** | **KPI** | **Meta SMART**  
    --- | --- | --- | ---  
    Aumentar a receita recorrente | Lançar novo SaaS com assinatura | Receita MRR | +35% até dez/2025  
    Reduzir custos operacionais | Automatizar processos com RPA | Custo operacional | -20% até set/2025  
    Melhorar satisfação do cliente | Implantar atendimento com IA | NPS | NPS 75 até nov/2025  
    """)
    st.markdown("🔄 [Retornar ao Topo](#topo) | 🔙 [Página Principal](#motiontech-solutions)")

def page4():
    st.title("💻 Papel da TI como Vantagem Competitiva")
    st.markdown("""
    A tecnologia é um fator estratégico essencial para MotionTech Solutions, permitindo inovação e eficiência operacional.  
    **Diferenciais tecnológicos:**  
    - Infraestrutura baseada em cloud computing  
    - Implementação de IA para automação inteligente  
    - Processos ágeis para entrega de software  
    """)
    st.markdown("🔄 [Retornar ao Topo](#topo) | 🔙 [Página Principal](#motiontech-solutions)")

def page5():
    st.title("📈 Balanced Scorecard")
    st.markdown("""
    **Indicador:** Número de Novos Clientes B2B  
    **Objetivo:** Ampliar a base de clientes B2B  
    **Fórmula:** Novos clientes adquiridos no período  
    **Meta SMART:** Crescimento de 40% até dez/2025  
    """)
    st.markdown("🔄 [Retornar ao Topo](#topo) | 🔙 [Página Principal](#motiontech-solutions)")

# Execução das páginas
pages = {
    "Página Principal": main_page,
    "Cenário da Empresa": page1,
    "Objetivos Estratégicos": page2,
    "Iniciativas, KPIs e Metas": page3,
    "Papel da TI": page4,
    "Balanced Scorecard": page5
}

selected_page = st.sidebar.selectbox("Navegação", pages.keys())
pages[selected_page]()

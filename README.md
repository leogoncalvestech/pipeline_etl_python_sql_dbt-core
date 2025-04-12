
flowchart TD
    %% Estilo e cores
    classDef startEnd fill:#e3f6f5,stroke:#2c7a7b,stroke-width:2px;
    classDef extract fill:#ffddd2,stroke:#e76f51,stroke-width:2px;
    classDef transform fill:#e0fbfc,stroke:#3d5a80,stroke-width:2px;
    classDef load fill:#fefae0,stroke:#d4a373,stroke-width:2px;

    %% Início e Fim
    A([🚀 Início]):::startEnd --> B[📥 Extrair Dados das Commodities]:::extract
    E[🏁 Fim]:::startEnd

    %% Subprocesso: Extração
    B --> B1[🔍 Buscar Dados de Cada Commodity]:::extract
    B1 --> B2[📄 Adicionar Dados na Lista]:::extract

    %% Subprocesso: Transformação
    B2 --> C[🔧 Transformar Dados das Commodities]:::transform
    C --> C1[🧩 Concatenar Todos os Dados]:::transform
    C1 --> C2[🧹 Preparar DataFrame]:::transform

    %% Subprocesso: Carga
    C2 --> D[💾 Carregar Dados no PostgreSQL]:::load
    D --> D1[📥 Salvar DataFrame no Banco]:::load

    D1 --> E

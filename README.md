'''mermaid
flowchart TD;
    A([Início]) --> B[Extrair Dados das Commodities]
    B --> B1[Buscar Dados de Cada Commodity]
    B1 --> B2[Adicionar Dados na Lista]
    B2 --> C[Transformar Dados das Commodities]
    C --> C1[Concatenar Todos os Dados]
    C1 --> C2[Preparar DataFrame]
    C2 --> D[Carregar Dados no PostgreSQL]
    D --> D1[Salvar DataFrame no Banco]
    D1 --> E([Fim])

    %% Agrupamentos visuais
    subgraph Extrair
        B
        B1
        B2
    end

    subgraph Transformar
        C
        C1
        C2
    end

    subgraph Carregar
        D
        D1
    end

'''
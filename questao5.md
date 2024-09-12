**Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.\
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.\
Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?**  

- Vamos nomear os interruptores como:
  - **i1, i2, i3**
- E renomear também as salas como:
  - **Sala1, Sala2, Sala3**

### Solução

> 1. Primeiro, acenderia o **i1**.
> 2. Aguardaria **8 minutos**.
> 3. Desligaria o **i1**.
> 4. Acenderia o **i2**.
> 5. Verificaria a **Sala1**:
>    - Se a lâmpada estiver apagada:
>      - Tocaria na lâmpada.
>        - Se a lâmpada estiver **QUENTE**:
>          - O **i1** é o interruptor correspondente àquela lâmpada.
>        - Se a lâmpada estiver **FRIA**:
>          - O **i2** ou **i3** pode ser o correspondente à lâmpada da **Sala1**.
> 6. Verificaria a **Sala2**:
>    - Se a lâmpada da **Sala1** estiver **FRIA**:
>      - Se a lâmpada da **Sala2** estiver apagada:
>        - A ordem respectiva dos interruptores é:
>          - **i1** pertence à **Sala2**.
>          - **i2** pertence à **Sala3**.
>          - **i3** pertence à **Sala1**.
>      - Se a lâmpada da **Sala2** estiver acesa:
>        - A ordem respectiva dos interruptores é:
>          - **i1** pertence à **Sala3**.
>          - **i2** pertence à **Sala2**.
>          - **i3** pertence à **Sala1**.
>    
>    - Se a lâmpada da **Sala1** estiver **QUENTE**:
>      - Se a lâmpada da **Sala2** estiver apagada:
>        - A ordem respectiva dos interruptores é:
>          - **i1** pertence à **Sala1**.
>          - **i2** pertence à **Sala3**.
>          - **i3** pertence à **Sala2**.
>      - Se a lâmpada da **Sala2** estiver acesa:
>        - A ordem respectiva dos interruptores é:
>          - **i1** pertence à **Sala1**.
>          - **i2** pertence à **Sala2**.
>          - **i3** pertence à **Sala3**.

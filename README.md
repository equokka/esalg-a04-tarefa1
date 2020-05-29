Esta resposta utiliza os seguintes pacotes:

```sh
pip install pyyaml faker
```

## Requisitos:

* [x] F1 – Gerar uma fila para a triagem. Para simular as respostas, podes atribuir de forma aleatória uma resposta afirmativa ou nenhuma (azul).
  * As Opções 1 gera pessoas e coloca-as na fila de espera.
* [x] F2 - Mostrar no ecrã o estado das filas do sistema.
  * O estado das filas está sempre visível.
* [x] F3 – Simular o atendimento de n (n > 0) pessoas da fila para a triagem. No atendimento de cada pessoa, o sistema deve atribuir-lhe uma prioridade e colocá-la na fila prioritária.
  * A Opção 3 passa as pessoas na fila de espera para a de triagem, dando-lhes uma prioridade.
* [x] F4 – Simular o atendimento de todas as pessoas que estão na fila para o atendimento clínico (prioritária), retirando cada pessoa da fila e mostrando no ecrã os dados dessa pessoa.
  * A Opção 4 simula o atendimento com prioridade das pessoas.

* Classes:
  * [ ] Sistema - N/A
  * [x] Pessoa - `Person`
  * [x] FilaPrioridade - `PersonHeap`
  * [x] Fila - `Queue`
  * [x] Amontoado - `Heap`

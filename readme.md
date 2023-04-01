# Projeto Fábrica de Software
Projeto de CRUD em Python e RestFramework com Banco de Dados PostgresQL. O projeto possui DUAS versões, uma onde há relacionamento entre as classes e outra sem. Cada pasta contém arquivo requirements.txt e de banco de dados. A pasta referente ao Virtual Envirement foi escondida por meio do .gitignore.

# DESAFIO_COM_RELACIONAMENTO
Nesta versão tentei implementar um CRUD para escritório de advocacia que recebe informações de Cliente e Advogado e *relaciona* com Processo.

*Cliente:* Na aba cliente, recebe os campos Nome, Endereço e Telefone (modelagem CharField) e o campo Email (modelagem EmailField). 

*Advogado:* recebe os campos Nome e Area (de atuação,modelagem CharField), Email (modelagem EmailField) e Telefone (Aqui utilizando a modelagem DecimalField com máximo de 12 dígitos e decimal_places=0).

*Processo:* recebe os campos Parte (que se relaciona com os clientes previamente cadastrados, utilizando modelagem ForeignKey), Numero(utilizando a modelagem DecimalField com máximo de 20 dígitos e decimal_places=0), Assunto (modelagem CharField), Criação (modelagem DateField para controle de data de inserção do processo no sistema), Ativo (modelagem BooleanField para acompanhamento de processos ativos ou não), Informações (modelagem TextField para informações extras acerca do processo) e Responsável (que se relaciona com os advogados previamente cadastrados, utilizando modelagem ForeignKey).

A modelagem ForeignKey com on_delete=models.DO_NOTHING faz com que DELETAR um advogado ou cliente que está vinculado a um processo retorne o Erro 500, evitando assim que seja possível deletar esses dados e resultar em um processo relacionado a um campo vazio no banco de dados. A razão para esta modelagem foi a segurança de que ainda que um Cliente ou Advogado encerre seu vínculo com o escritório, seus dados continuarão no banco de dados da empresa.

Em serializer foi necessário utilizar o método SerializerMethodField para que o nome da parte e do advogado responsável ficassem visiveis para os usuários. Ainda, fez-se implementação das funções get_parte_nome e get_responsável_nome.

As rotas foram definidas por meio do routers em 'url.py' e os Viewsets são guiados pelas classes acima descritas.

Os nomes de arquivos e pastas foram mantidos o mais intuitivo possível para uma fácil navegação no código e se adequando as necessidades reais de um sistema de escritorio de advocacia.



#  DESAFIO_SEM_RELACIONAMENTO
Nesta versão tentei implementar um CRUD para escritório de advocacia que recebe informações de Cliente e Advogado e *NÃO* há relacionamento com Processo.

*Cliente:* Na aba cliente, recebe os campos Nome, Endereço (modelagem CharField), Telefone (modelagem DecimalField com máximo de 12 dígitos e decimal_places=0) e o campo Email (modelagem EmailField). 

*Advogado:* recebe os campos Nome e Area (de atuação,modelagem CharField), Email (modelagem EmailField) e Telefone (modelagem DecimalField com máximo de 12 dígitos e decimal_places=0).

*Processo:* recebe os campos Parte e Advogado Responsável (modelagem CharField), Numero(utilizando a modelagem DecimalField com máximo de 20 dígitos e decimal_places=0), Assunto (modelagem CharField), Criação (modelagem DateField para controle de data de inserção do processo no sistema), Ativo (modelagem BooleanField para acompanhamento de processos ativos ou não) e Informações (modelagem TextField para informações extras acerca do processo).

Aqui *não há relacionamento* entre as classes, sendo possível apagar os dados de Cliente e Advogado sem influenciar na classe Processo.

As rotas foram definidas por meio do routers em 'url.py' e os Viewsets são guiados pelas classes acima descritas.

Os nomes de arquivos e pastas foram mantidos o mais intuitivo possível para uma fácil navegação no código e se adequando as necessidades reais de um sistema de escritorio de advocacia.

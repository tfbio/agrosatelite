# Agrosatélite Farm Project Front e Back

Olá Agrosatélite TI e IEL,

O desenvolvimento do Backend seguiu todos os pontos de 1. a 5. fazendo alterações em arquivos relevantes: models, serializers, filters e migrations.
Além disso, incluí testes automatizados para testar as rotas da API editadas: Farm GET List, GET details para as edições 4. e 5. e Farm_POST para verificar a criação de farms sem campos obrigatórios, restrição solicitada em 2., pois isto é uma boa prática de desenvolvimento de software junto com a proteção de informações sensíveis, como SECRET_KEY em settings.py, que poderia ser definida em uma variável ambiente .env.

E o desenvolvimento do Frontend seguiu todas as histórias de usuários do 1 ao 5.3 e a 6, opcional.
A única alteração extra para completar a requisição 1 a 6 que achei importante foi incluir o campo id ao farm model, informação que já existe no banco de dados como autoincremento agora é mostrada em requisições/respostas e, por exemplo, é útil na atualização e exclusão por operações CRUD por se ter um confiável identificador único para cada fazenda, pois outros campos name, goemetry, centroid, state, municipality não estão definidos como únicos no momento.

# Agrosatelite Farm Project Front and Back

Hello Agrosatelite TI and IEL,

Development done on Backend followed all the points from 1. to 5. making changes to relevant files: models, serializers, filters and migrations.
Also, I included automated tests for testing the edited API routes: Farm GET List, GET details for the edits 4. and 5. and Farm_POST to verify creation of farm without mandatory fields, restriction requested in 2., as it is a good pratice of software development along with protecting sensitive information, like SECRET_KEY in settings.py, in a .env environment variable

And development done on Frontend followed all user stories from 1 to 5.3 and the optional 6.
Only extra change for completing request 1 to 6 I deemed important was to add field id to the farm model, information that already exists in the database now it is shown in request/response and, for example, it is important in CRUD update and delete operation by having a truly unique identifier for each farm, as other farm fields name, goemetry, centroid, state, municipality are not set to be unique at the moment.




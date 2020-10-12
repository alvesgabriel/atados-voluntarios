[ ~ Dependencies scanned by PyUp.io ~ ]

# atados-voluntarios

[![Updates](https://pyup.io/repos/github/alvesgabriel/atados-voluntarios/shield.svg)](https://pyup.io/repos/github/alvesgabriel/atados-voluntarios/)
[![Python 3](https://pyup.io/repos/github/alvesgabriel/atados-voluntarios/python-3-shield.svg)](https://pyup.io/repos/github/alvesgabriel/atados-voluntarios/)
[![codecov](https://codecov.io/gh/alvesgabriel/atados-voluntarios/branch/main/graph/badge.svg)](https://codecov.io/gh/alvesgabriel/atados-voluntarios)


## Rodando Aplicação com o Docker

### Iniciando Aplicação

*Obs: Para executar o projeto com os comandos a seguir é necessário ter o `docker` e `docker-compose` instalados no seu ambiente.*

```shell
docker-compose up -d
```

### Migração

```shell
docker exec -d voluntarios_web python manage.py migrate
```

### Criacao de super usuário

```shell
docker exec -it voluntarios_web /bin/bash
python manage.py createsuperuser
```

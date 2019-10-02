# Crawler

## Descrição

Crawler que coleta várias informações sobre subreddits linkados em postagens no subreddit [r/EmPortugues](https://www.reddit.com/r/EmPortugues/).

O crawler confere a lista de subreddits e utiliza [PRAW](https://praw.readthedocs.io/en/latest/#) em modo somente leitura para obter dados dos subreddits publicados no subreddit utilizando [Reddit JSON API](https://github.com/reddit-archive/reddit/wiki/json) e serializar os dados num arquivo JSON além de salvar subreddits privados ou banidos da lista em arquivos TXT.

A coleta de dados processada pelo crawler possibilita a leitura de baixo para cima da lista com `reversed()` registrando subreddits privados e banidos em listas diferentes com `Exception` e serializando dados extraídos dos subreddits listados num arquivo JSON com `DataObject()` e `json.dumps` além de registrar a data com `datetime`.

As informações salvas pelo crawler são: `display_name_prefixed`, `community_icon`, `public_description`, `subscribers`, `created`, `over18`, `moderator()` e `comment.list` e `datetime.now()`.

## Sumário
* [Instalação](#Instalação)
* [Instruções](#Instruções)
* [Dependências](#Dependências)
* [Colaboração](#Colaboração)
* [Referências](#Referências)

## Instalação
1. Clone o repositório;
2. execute um interpretador de comandos;
3. navegue até a pasta;
4. e rode `py start.py`.

## Instruções
Para alterar o caminho da lista, em [crawler.py](https://github.com/subreddit-emportugues/crawler/blob/master/crawler.py), edite:
```
for name in reversed(open('../data/subreddits.txt').readlines()):
```

Para alterar as chaves do objeto JSON, em [subreddit.py](https://github.com/subreddit-emportugues/crawler/blob/master/subreddit.py), edite:
```
def __init__(self, id, name, icon, description, members, age, nsfw, moderators, recent_submissions, recent_comments):
    self.id = id
    self.name = name
    self.icon = icon
    self.description = description
    self.members = members
    self.age = age
    self.nsfw = nsfw
    self.moderators = moderators
    self.recent_submissions = recent_submissions
    self.recent_comments = recent_comments
```

Para alterar os valores do objeto JSON, em [crawler.py](https://github.com/subreddit-emportugues/crawler/blob/master/crawler.py), edite:
```
def define_subreddit(self, subreddit_model, moderators, recent_submissions, recent_comments):
    subreddit = Subreddit(
        self.data_object.get_length(),
        subreddit_model.display_name_prefixed,
        subreddit_model.community_icon,
        subreddit_model.public_description,
        subreddit_model.subscribers,
        subreddit_model.created,
        subreddit_model.over18,
        moderators,
        recent_submissions,
        recent_comments
    )
```

## Dependências
> PRAW
```
import praw
```
> json
```
import json
```
> time
```
import time
```
> datetime
```
import datetime
```

## Colaboração

Você pode colaborar com o desenvolvimento deste repositório!

[Confira os kanbans deste projeto](https://github.com/orgs/subreddit-emportugues/projects/2), [entre em contato com a equipe de moderação](https://reddit.com/message/compose?to=/r/EmPortugues) e [participe da equipe de desenvolvimento](https://github.com/orgs/subreddit-emportugues/teams/desenvolvedores) para saber a respeito do progresso deste repositório caso queira colaborar antes de [reportar um novo problema](https://github.com/subreddit-emportugues/aplicativo/issues) ou [solicitar o recebimento de uma modificação](https://github.com/subreddit-emportugues/aplicativo/pulls).

## Referências

* Crawler: https://github.com/subreddit-emportugues/crawler/blob/master/start.py
* Comunidade: https://www.reddit.com/r/EmPortugues
* Organização: https://github.com/subreddit-emportugues
* Repositório: https://github.com/subreddit-emportugues/crawler
* Projeto: https://github.com/orgs/subreddit-emportugues/projects/2
* Equipe: https://github.com/orgs/subreddit-emportugues/teams/desenvolvedores
* Licença: 

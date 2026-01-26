# Tuva EMPI

## Docs

https://tuva-health.github.io/tuva_empi/docs/

## Getting Started with Local Development

https://tuva-health.github.io/tuva_empi/docs/contribute/local-development/common-setup

```
cp .env.example .env

cp backend/config/local.json.example backend/config/local.json

go to localhost:3000
```

ssh \
  -L 4566:localhost:4566 \
  -L 5432:localhost:5432 \
  -L 8000:localhost:8000 \
  -L 3000:localhost:3000 \
sandbox004-notebook

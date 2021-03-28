#!/usr/bin/env bash

npx husky add .github/husky/commit-msg "npm cm"
npx husky add .github/husky/pre-commit "npm secrets"

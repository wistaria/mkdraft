#!/bin/sh

if [ -d ${HOME}/venv/mkdraft ]; then :; else
  python3 -m venv ${HOME}/venv/mkdraft
  . ${HOME}/venv/mkdraft/bin/activate
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
fi

#!/bin/bash
# Wrapper script for Ansible Python interpreter
# This handles paths with spaces correctly
exec "/home/taha/Code/DevOps presentation/ansible-k8s-demo/myvenv/bin/python3" "$@"


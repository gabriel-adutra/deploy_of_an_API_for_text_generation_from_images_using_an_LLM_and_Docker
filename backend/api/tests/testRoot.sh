#!/bin/bash

# Test script for the root endpoint (/)
echo "Testing root endpoint..."
curl -X GET "http://localhost:3000/" -H "accept: application/json"


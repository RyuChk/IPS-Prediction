PYTHON ?= python3

.dependency:
	@printf \\e[1m"Install dependency"\\e[0m\\n
	@$(PYTHON) -m pip install grpc-stubs
	@$(PYTHON) -m pip install grpcio-tools
	@$(PYTHON) -m pip install openpyxl

.generate_model:
	@printf \\e[1m"Generate model from code"\\e[0m\\n
	@rm -rf model/cmkl_model.pkl
	@$(PYTHON) model/cmklmodel.py

generate: .dependency .generate_model
	@printf \\e[1m"Generate gRPC code"\\e[0m\\n
	@rm -rf ips 
	@find proto -name '*.proto' -exec $(PYTHON) -m grpc_tools.protoc \
      -I proto \
      --python_out=. \
      --grpc_python_out=. \
      {} +

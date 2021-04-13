build-HyperGrowthLayer:
	( cd hypergrowth; tox )
	( cd example_shared; tox)
	( cd example; tox)
	mkdir -p "$(ARTIFACTS_DIR)/"
	python -m pip install hypergrowth/.tox/dist/* example_shared/.tox/dist/* example/.tox/dist/* -t "$(ARTIFACTS_DIR)/python"
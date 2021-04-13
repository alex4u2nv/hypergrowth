build-HyperGrowthLayer:
	( cd hypergrowth; tox )
	( cd example_shared; tox)
	( cd example; tox)
	mkdir -p "$(ARTIFACTS_DIR)/"
	mkdir -p "/tmp/artifacts/"
	cp hypergrowth/.tox/dist/* example_shared/.tox/dist/* example/.tox/dist/* /tmp/artifacts/
	python -m pip install /tmp/artifacts/* -t "$(ARTIFACTS_DIR)/python"
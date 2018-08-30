OUTPUT_DIR:=$(shell pwd)

fix-async:
	echo "$(OUTPUT_DIR)"
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" 's/async=/async_req=/g' {} +
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" 's/async bool/async_req bool/g' {} +
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" "s/'async'/'async_req'/g" {} +
	sed -i "" "s/if not async/if not async_req/g" "$(OUTPUT_DIR)/swagger_client/api_client.py"
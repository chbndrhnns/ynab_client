OUTPUT_DIR:=$(shell pwd)

fetch-swagger-file:
	curl -o spec-v1-swagger.json https://api.youneedabudget.com/papi/spec-v1-swagger.json

allow-null:
	sed -E -i '' 's/\: \"(string|number|integer|array|boolean)\"+/\: [\"\1\",\"null\"]/g' spec-v1-swagger.json

fix-async:
	echo "$(OUTPUT_DIR)"
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" 's/async=/async_req=/g' {} +
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" 's/async bool/async_req bool/g' {} +
	find "$(OUTPUT_DIR)/swagger_client/" -type f -name \*.py -exec sed -i "" "s/'async'/'async_req'/g" {} +
	sed -i "" "s/if not async/if not async_req/g" "$(OUTPUT_DIR)/swagger_client/api_client.py"

client-allow-null: clean fetch-swagger-file allow-null
	swagger-codegen generate -i spec-v1-swagger.json -l python -o .

client: clean fetch-swagger-file
	swagger-codegen generate -i spec-v1-swagger.json -l python -o .

clean:
	rm -rf swagger_client* test docs

generate-3.7: client fix-async
	echo "all"%
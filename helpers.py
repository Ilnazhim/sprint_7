import allure


def validate_schema(schema, response):
    with allure.step(f"Validate schema {schema.__name__}"):
        schema.model_validate(response)

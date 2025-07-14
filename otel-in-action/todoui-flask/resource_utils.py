from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.attributes import service_attributes

def create_resource(name: str, version: str) -> Resource:
    svc_resource = Resource.create(
        {
            service_attributes.SERVICE_NAME: name,
            service_attributes.SERVICE_VERSION: version
        }
    )
    return svc_resource
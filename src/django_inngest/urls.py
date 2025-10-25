import inngest
import inngest.django

from .client import inngest_client
from .discovery import discover_inngest_functions

inactive_inngest_functions = ["test/inactive/discovery"]

# Automatically discover all Inngest functions, excluding inactive ones
active_inngest_functions = discover_inngest_functions(
    inngest_client=inngest_client, inactive_function_ids=inactive_inngest_functions
)

inngest_url = inngest.django.serve(inngest_client, active_inngest_functions)
inngest_urls = [inngest_url]

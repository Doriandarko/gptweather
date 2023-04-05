In this tutorial, we will create a simple to-do list plugin using OpenAI's new plugin system. We will be using Python and deploying the plugin on Replit. The plugin will be authenticated using a service level authentication token and will allow users to create, view, and delete to-do items. We will also be defining an OpenAPI specification to match the endpoints defined in our plugin.

## ChatGPT Plugins

The ChatGPT plugin system enables language models to interact with external tools and services, providing access to information and enabling safe, constrained actions. Plugins can address challenges associated with large language models, including keeping up with recent events, accessing up-to-date information, and providing evidence-based references to enhance the model's responses.

Plugins also enable users to assess the trustworthiness of the model's output and double-check its accuracy. However, there are also risks associated with plugins, including the potential for harmful or unintended actions.

The development of the ChatGPT plugin platform has included several safeguards and red-teaming exercises to identify potential risks and inform safety-by-design mitigations. The deployment of access to plugins is being rolled out gradually, and researchers are encouraged to study safety risks and mitigations in this area. The ChatGPT plugin system has wide-ranging societal implications and may have a significant economic impact.

Learn more or signup here: [https://openai.com/blog/chatgpt-plugins](https://openai.com/blog/chatgpt-plugins)

## Prerequisites

To complete this tutorial, you will need the following:

* A basic understanding of Python
* A Replit account (you can sign up for free at replit.com)
* An OpenAI API key (you can sign up for free at openai.com)
* A text editor or the Replit IDE

## Replit

[Replit](https://replit.com/) is an online integrated development environment (IDE) that allows you to code in many programming languages, collaborate with others in real-time, and host and run your applications in the cloud. It's a great platform for beginners, educators, and professionals who want to quickly spin up a new project or prototype, or for teams who want to work together on code.

## Plugin Flow:

1. **Create a manifest file**: Host a manifest file at yourdomain.com/.well-known/manifest.json, containing metadata about the plugin, authentication details, and an OpenAPI spec for the exposed endpoints.
2. **Register the plugin in ChatGPT UI**: Install the plugin using the ChatGPT UI, providing the necessary OAuth 2 client\_id and client\_secret or API key for authentication.
3. **Users activate the plugin**: Users manually activate the plugin in the ChatGPT UI. During the alpha phase, developers can share their plugins with 15 additional users.
4. **Authentication**: If needed, users are redirected via OAuth to your plugin for authentication, and new accounts can be created.
5. **Users begin a conversation**: OpenAI injects a compact description of the plugin into the ChatGPT conversation, which remains invisible to users. The model may invoke an API call from the plugin if relevant, and the API results are incorporated into its response.
6. **API responses**: The model may include links from API calls in its response, displaying them as rich previews using the OpenGraph protocol.
7. **User location data**: The user's country and state are sent in the Plugin conversation header for relevant use cases like shopping, restaurants, or weather. Additional data sources require user opt-in via a consent screen.


Just replace your API for OpenWeather

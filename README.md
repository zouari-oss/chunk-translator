<!-- PROJECT SHIELDS -->

[![Contributors](https://img.shields.io/badge/CONTRIBUTORS-01-blue?style=plastic)](https://github.com/ZouariOmar/AgriGO/graphs/contributors)
[![Forks](https://img.shields.io/badge/FORKS-00-blue?style=plastic)](https://github.com/ZouariOmar/AgriGO/network/members)
[![Stargazers](https://img.shields.io/badge/STARS-01-blue?style=plastic)](https://github.com/ZouariOmar/AgriGO/stargazers)
[![Issues](https://img.shields.io/badge/ISSUES-00-blue?style=plastic)](https://github.com/ZouariOmar/AgriGO/issues)
[![GPL3.0 License](https://img.shields.io/badge/LICENSE-GPL3.0-blue?style=plastic)](LICENSE)
[![Linkedin](https://img.shields.io/badge/Linkedin-6.9k-blue?style=plastic)](https://www.linkedin.com/in/zouari-omar-143239283)

<!-- PROJECT HEADER -->
<h1 align="center">
  <br>
  <a href="https://github.com/zouari-oss/chunk-translator"><img src="res/logo-without-bkg.png" alt="chunk-translator" width="400"></a>
  <br>
  chunk-translator
  <br>
</h1>

<h4 align="center">FastAPI endpoint for chunked text translation</h4>

<!-- PROJECT LINKS -->
<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#emailware">Emailware</a> •
  <a href="#license">License</a> •
  <a href="#contact">Contact</a> •
  <a href="#acknowledgments">Acknowledgments</a>
</p>

<!-- PROJECT TAGS -->
<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/API-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="API">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/REST-02569B?style=for-the-badge&logo=api&logoColor=white" alt="REST API">
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  <img src="https://img.shields.io/badge/Open%20Source-3DA639?style=for-the-badge&logo=opensourceinitiative&logoColor=white"/>
</p>

## Overview

**chunk-translator** is a lightweight API built with **FastAPI** that translates large text safely by splitting it into manageable chunks.

Many translation models or APIs fail when processing very large inputs. This project solves that by:

- Splitting large text into chunks
- Translating each chunk independently
- Reassembling the translated output in the correct order

> The result is reliable translation **without losing lines or breaking formatting**.

## Key Features

- **FastAPI powered REST API**
- **Automatic text chunking**
- **Supports large document translation**
- **Reassembles chunks in correct order**
- **Prevents dropped lines during translation**
- **Simple JSON API interface**
- **Easy to integrate into pipelines**

## Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API

```bash
fastapi run
```

### 3. Use `/translate`

<details open>
<summary><strong>curl</strong></summary>

```bash
curl -s \
  --header "Content-Type: application/json" \
  --request "POST" \
  --data '{
    "text": "Hello world",
    "source_lang": "en",
    "target_lang": "fr"
  }' \
  http://127.0.0.1:8000/translate
```

</details>

<details>
<summary><strong>JavaScript (js)</strong></summary>

```js
const response = await fetch("http://127.0.0.1:8000/translate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    text: "Hello world",
    source_lang: "en",
    target_lang: "fr",
  }),
});

const data = await response.json();
console.log(data);
```

</details>

<details>
<summary><strong>Java</strong></summary>

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class TranslateClient {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String json = """
            {
              "text": "Hello world",
              "source_lang": "en",
              "target_lang": "fr"
            }
            """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("http://127.0.0.1:8000/translate"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(json))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```

</details>

<details>
<summary><strong>C</strong></summary>

```c
#include <curl/curl.h>

int main(void) {
  CURL *curl = curl_easy_init();
  if (!curl) return 1;

  const char *json =
    "{\"text\":\"Hello world\",\"source_lang\":\"en\",\"target_lang\":\"fr\"}";

  struct curl_slist *headers = NULL;
  headers = curl_slist_append(headers, "Content-Type: application/json");

  curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:8000/translate");
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json);
  curl_easy_setopt(curl, CURLOPT_POST, 1L);
  curl_easy_perform(curl);

  curl_slist_free_all(headers);
  curl_easy_cleanup(curl);
  return 0;
}
```

</details>

<details>
<summary><strong>C++ (cpp)</strong></summary>

```cpp
#include <curl/curl.h>
#include <string>

int main() {
  CURL* curl = curl_easy_init();
  if (!curl) return 1;

  std::string json =
    R"({"text":"Hello world","source_lang":"en","target_lang":"fr"})";

  struct curl_slist* headers = nullptr;
  headers = curl_slist_append(headers, "Content-Type: application/json");

  curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:8000/translate");
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json.c_str());
  curl_easy_setopt(curl, CURLOPT_POST, 1L);
  curl_easy_perform(curl);

  curl_slist_free_all(headers);
  curl_easy_cleanup(curl);
  return 0;
}
```

</details>

### 4. Example Response

```JSON
{
  "status": 200,
  "translated_text": "Translated output..."
}
```

## Emailware

chunk-translator is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <zouariomar20@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## License

This repository is licensed under the **GPL-3.0 License**. You are free to use, modify, and distribute the content. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out:

- **GitHub**: [ZouariOmar](https://github.com/ZouariOmar)
- **Email**: <zouariomar20@gmail.com>
- **LinkedIn**: [Zouari Omar](https://www.linkedin.com/in/zouari-omar)

## Acknowledgments

Built with ❤️ for the open source community

> **Happy Coding!**

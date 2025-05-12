# Privacy Policy for Edge-TTS Plugin

## Overview

The Edge-TTS plugin for Dify uses Microsoft Azure's Text-to-Speech (TTS) service to synthesize speech from user-provided
text. This plugin is designed with privacy in mind and does not collect, store, or transmit any personally identifiable
information (PII).

## Data Usage

- **Text Input**: The plugin receives plain text input from the user, along with parameters such as language, voice, and
  audio format.
- **Processing**: This text is sent to Microsoft Azure's TTS API to generate the corresponding audio. The processing
  occurs over a secure HTTPS connection.
- **Output**: The synthesized audio is returned to the user via Dify. No data is stored locally or sent to any
  third-party server other than Microsoft Azure.

## Data Retention

- The plugin does **not** retain any user data, text input, audio output, or request logs.
- All requests are processed in real-time and discarded after the response is returned.

## Third-Party Services

This plugin interacts **only** with Microsoft Azure Cognitive Services. For more information about Microsoft's handling
of data, please refer to:

- [Microsoft Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)

## Compliance

This plugin complies with the Dify Plugin Privacy Protection Guidelines. It does not collect or process the following:

- Names
- Email addresses
- Phone numbers
- IP addresses
- Geolocation
- User account data

## Contact

For any questions regarding privacy or data handling in this plugin, please contact the plugin author
via [GitHub Issues](https://github.com/ZZM-user/edge_tts/issues).

---

_Last updated: May 2025_

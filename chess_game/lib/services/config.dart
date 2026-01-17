import 'package:flutter/foundation.dart';

class AppConfig {
  static const String _productionHost = 'chess-game-app-production.up.railway.app';

  static String get baseUrl {
    if (kIsWeb) return 'http://127.0.0.1:8000/api/auth/';
    // Production Railway URL
    return 'https://$_productionHost/api/auth/';
  }

  static String get socketUrl {
    if (kIsWeb) return "ws://127.0.0.1:8000/ws/call/";
    // Production Railway URL
    return "wss://$_productionHost/ws/call/";
  }
}

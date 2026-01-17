import 'package:flutter/foundation.dart';

class AppConfig {
  static const String _productionHost = 'chessgameapp.up.railway.app';

  static String get baseUrl {
    // Use Railway URL for both web and mobile in production
    return 'https://$_productionHost/api/auth/';
  }

  static String get socketUrl {
    // Use Railway WebSocket URL for both web and mobile in production
    return "wss://$_productionHost/ws/call/";
  }
}

import 'package:flutter/material.dart';
import 'package:augmented_reality_plugin/augmented_reality_plugin.dart';

class AugmentedRealityView extends StatefulWidget {
  final String img;


  AugmentedRealityView({required this.img});

  @override
  _AugmentedRealityViewState createState() => _AugmentedRealityViewState();
}

class _AugmentedRealityViewState extends State<AugmentedRealityView> {
  @override
  Widget build(BuildContext context) {
    return AugmentedRealityPlugin(
        'https://5831-2409-4073-414-1c17-c044-5ad9-2a48-1d74.ngrok-free.app${widget.img}'
    );
  }
}

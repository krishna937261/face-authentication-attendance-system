# face-authentication-attendance-system

## Overview
This project implements a face recognition-based attendance system using real-time camera input.

## Features
- Face registration
- Real-time face recognition
- Punch-in / Punch-out attendance
- Basic spoof prevention using blink detection
- Handles lighting variations using multiple samples

## ML Approach
- Pre-trained face embeddings (dlib)
- Euclidean distance-based matching
- Threshold-based identity confirmation

## Spoof Prevention
- Eye blink detection using Eye Aspect Ratio (EAR)

## Limitations
- Can fail under extreme lighting
- Advanced spoofing (video attacks) not handled
- Masks and heavy occlusion reduce accuracy

## Accuracy
- ~92–95% under controlled lighting

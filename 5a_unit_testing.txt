import unittest
import emotion_detection as ed

class EmotionDetectionTest(unittest.TestCase):
    
    JOY = "I am glad this happened"
    ANGER = "I am really mad about this"
    DISGUST = "I feel disgusted just hearing about this"
    SADNESS = "I am so sad about this"
    FEAR = "I am really afraid that this will happen"
    
    def test_emotion_joy(self):
        expected = 'joy'
        found = ed.emotion_detector(self.JOY)['dominant_emotion']
        self.assertEqual(found, expected)

    def test_emotion_anger(self):
        expected = 'anger'
        found = ed.emotion_detector(self.ANGER)['dominant_emotion']
        self.assertEqual(found, expected)
    
    def test_emotion_disgust(self):
        expected = 'disgust'
        found = ed.emotion_detector(self.DISGUST)['dominant_emotion']
        self.assertEqual(found, expected)
    
    def test_emotion_sadness(self):
        expected = 'sadness'
        found = ed.emotion_detector(self.SADNESS)['dominant_emotion']
        self.assertEqual(found, expected)
    
    def test_emotion_fear(self):
        expected = 'fear'
        found = ed.emotion_detector(self.FEAR)['dominant_emotion']
        self.assertEqual(found, expected)

if __name__ == '__main__':
    unittest.main()
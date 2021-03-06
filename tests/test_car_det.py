import tensorflow as tf
from object_detection import tf_hub_sample


def test_loading_model_from_tf_hub(coco_labels):
	tf_hub_det = tf_hub_sample.TfHubSampleDetector(coco_labels_path=coco_labels)
	output = tf_hub_det.detector(tf.ones((1, 256, 256, 3), tf.uint8))
	assert output["detection_anchor_indices"].numpy().shape == (1, 100)


def test_cars_detection(sample_image, coco_labels):
	tf_hub_det = tf_hub_sample.TfHubSampleDetector(coco_labels_path=coco_labels)
	image = tf_hub_det.load_image(sample_image)
	image_tensor = tf_hub_det.prepare_image(image)
	output = tf_hub_det.detector(image_tensor)
	detection_scores = output['detection_scores'].numpy()
	assert (detection_scores > 0.5).sum() == 3

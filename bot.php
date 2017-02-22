<?p
$acces_tken = '1XvzTYDBQ/aCf6BZ/0JtbhHzdeAJzgCbTehPsx+n+eyXBiyPJw9tHCd6ktqqUnj0vorYI39lJux/oGfscxvSS72Gln1UO8kUfL1+nthpyj4fZPSCBMkRup7+5pajYZ9Js/Jf16s2vjtIzHEuME6OSwdB04t89/1O/w1cDnyilFU=';
// Get POST body content
$content = file_get_contents('php://input');
// Parse JSON
$events = json_decode($content, true);
// Validate parsed JSON data
if (!is_null($events['events'])) {
	// Loop through each event
	foreach ($events['events'] as $event) {
		// Reply only when message sent is in 'text' format
		if ($event['type'] == 'message' && $event['message']['type'] == 'text') {
			// Get text 
			$text = str_replace("\n", " ", trim($event['message']['text']));
			
			// Get replyToken
			$replyToken = $event['replyToken'];
			// Python Execute
			$command = "LANG=en_US.UTF-8 PYTHONIOENCODING=utf-8 python3 ./python/chat.py " . escapeshellarg($text) . " 2>&1";
 			$response_message = shell_exec($command);
 			$response_message = trim($response_message);

			// Build message to reply back
			$messages = [
				'type' => 'text',
				'text' => $response_message
			];

			// Make a POST Request to Messaging API to reply to sender
			$url = 'https://api.line.me/v2/bot/message/reply';
			$data = [
				'replyToken' => $replyToken,
				'messages' => [$messages],
			];
			$post = json_encode($data);
			$headers = array('Content-Type: application/json', 'Authorization: Bearer ' . $access_token);

			$ch = curl_init($url);
			curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
			curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
			$result = curl_exec($ch);
			curl_close($ch);

			echo $result . "\r\n";
		}
	}
}
echo "OK";

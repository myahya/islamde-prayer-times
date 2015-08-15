export ISLAMDE=/Users/myahya/git-clients/islamde-prayer-times/

cat <<EOT > ~/Library/LaunchAgents/org.myahya.islamde-prayer-times.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
		<string>org.myahya.islamde-prayer-times</string>
	<key>ProgramArguments</key>
		<array>
			<string>/Users/myahya/git-clients/islamde-prayer-times/islamde-prayertimes.py</string>
		</array>
    <key>UserName</key>
      <string>myahya</string>

    <key>RunAtLoad</key>
      <true/>

	<key>StandardInPath</key>
	<string>/tmp/test.stdin</string>
	<key>StandardOutPath</key>
	<string>/tmp/test.stdout</string>
	<key>StandardErrorPath</key>
	<string>/tmp/test.stderr</string>

    <key>EnvironmentVariables</key>
		<dict>
			<key>ISLAMDE</key>
			<string>/Users/myahya/git-clients/islamde-prayer-times/</string>
		</dict>
</dict>
</plist>
EOT

launchctl load ~/Library/LaunchAgents/org.myahya.islamde-prayer-times.plist
#launchctl unload ~/Library/LaunchAgents/org.myahya.islamde-prayer-times.plist
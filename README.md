# Assetto Corsa Plugin for Prismatik
![Prismatik-iRacing-Feature](https://i.imgur.com/FN3yx5b.jpg)
This plugin allows you to visualize data from iRacing with an ambilight. It connects Prismatik to the iRacing API, enabling you to visualize information from the simulation in real-time. In the image above, the ambilight is acting as a shift light.

You can edit the configuration file to change the the mapped variable, the range, pattern, colors, and more. There are a number of presets available for common mappings such as shift lights or throttle/brake input, and you can make your own by saving your configuration file to the `presets` folder.

#### More Information:
[Blog Post](http://www.partsnotincluded.com/programming/iracing-plugin-for-prismatik)\
[YouTube Demo](https://www.youtube.com/watch?v=3TQP2Cu5w0k)

## Installation
1. [Download the plugin](../../releases/latest) and unzip it. Place the contained folder (*without* the version number) into your `Prismatik\Plugins` directory, located in your user folder.
2. Open Prismatik. Switch to the 'Experimental' page and click the checkbox to enable the API server. If you have an authorization key set you'll need to add it to the plugin's `config.ini` settings file.
3. Switch to the 'Plugins' page. At the top, click the "reload plugins" button and then click the checkbox to activate the iRacing plugin. If everything is set up properly the plugin status will switch to "(running)".

## Configuration
Modify the `config.ini` file with your settings. This is where you set the Prismatik API login and the variable to poll from iRacing, as well as the pattern and color information for the ambilight.

You can also set a preset in the "User Settings" section. More information on presets is available in [the presets README](presets/README.md). Note that any user settings in `config.ini` will overwrite their preset value.

```
[Prismatik]
# make sure to enable the API server in the Prismatik settings
host: 127.0.0.1
port: 3636
key:

[iRacing]
var: ShiftLight
var_min: 0.0
var_max: 1.0

[User Settings]
preset: ShiftLight
fps: 60
pattern: symmetric
colors: #00FF00, #FFFF00, #FF0000
off_color: #000000
single_color: false
bidirectional_color: false
blink_rate: 2.5
color_smoothing: true
data_filtering: low
```

### Prismatik:
* **host:** IP for the Prismatik installation you want to use. Default is the loopback address.
* **port:** socket port, set in Prismatik.
* **key:** (optional) API authentication key, set in Prismatik.

### iRacing:
* **var:** the variable being polled from *iRacing* to map to the LEDs. Works best with percentage-based variables such as Throttle, Brake, and ShiftLight.
* **var_min:** minimum value from the variable for mapping. Necessary for variables that aren't percentage-based.
* **var_max:** max value from the variable, same as above.

### User Settings:
These options can be customized to your liking, depending on how you want the lights to look.
* **preset:** chosen settings preset. You can find a list of presets [here](presets.md).
* **fps:** update rate for the API data and LED frames. *iRacing* API data is limited to a max of 60 fps.
* **pattern:** LED mapping pattern. Options: all, symmetric, clockwise, counter-clockwise, or bidirectional.
* **colors:** comma-separated list of RGB colors as [hex triplets](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet). Ordered from low mapped value to high.
* **off_color:** the 'zero' color that fills the rest of the LEDs. Usually black, but it's available to change if you want to.
* **single_color:** boolean for whether to use a single color for all LEDs per frame, or whether to use multiple colors mapped based on LED position.
* **bidirectional_color:** if true, scales the color array so both sides of the bidirectional pattern will display the same colors. If false, allows different colors on either side. Only used with the bidirectional pattern and single color mode.
* **blink_rate**: blinking speed of the LEDs if they're past the max value, in Hertz. Set to 0 or 'off' to disable blinking entirely.
* **color_smoothing:** when enabled, adds a linear fade between colors for a smooth transition. If disabled, color transitions are abrupt.
* **data_filtering:** weight towards the new value for the low-pass filter. Can either be set as a preset (none, low, medium, high) or as a float value from 0 - 1. Smaller values will give smoother but less-responsive results.

## Disclaimer
This is an unofficial plugin. The author is not affiliated with or supported by iRacing.com Motorsport Simulations.

## License
This plugin is licensed under the terms of the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

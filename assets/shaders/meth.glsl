#version 330 core

uniform sampler2D tex;
uniform float time;
uniform float luma;

in vec2 uvs;
out vec4 f_color;

vec3 rgb2hsv(vec3 c, float hueshift) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)) + hueshift, d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec3 process(vec3 color, vec2 uvs) {
	return hsv2rgb(rgb2hsv(color, uvs.x * uvs.y + time));
}

void main() {
	vec2 sample_pos = vec2(uvs.x + sin(uvs.y * 10 + time * 0.01) * 0.05, uvs.y);
	float r = texture(tex, sample_pos).r * luma;
	float g = texture(tex, sample_pos).g * luma;
	float b = texture(tex, sample_pos).b * luma;
	f_color = vec4(process(vec3(r, g, b), uvs), 1.0);
}
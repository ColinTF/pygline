# version 330 core

layout(location = 0) in vec2 a_postion;
//layout(location = 1) in vec3 a_color;

out vec3 v_color;

void main() {
    gl_Position = vec4(a_postion, 0.0, 1.0);
    v_color = vec3(1.0);
}
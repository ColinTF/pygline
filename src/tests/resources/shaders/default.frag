# version 330 core

out vec4 out_color;

in vec3 v_color;

void main() {
    out_color = vec4(v_color, 1.0);
}
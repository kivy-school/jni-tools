from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GL11:
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ADD_SIGNED: ClassVar[int]
    GL_ALPHA_SCALE: ClassVar[int]
    GL_ALPHA_TEST_FUNC: ClassVar[int]
    GL_ALPHA_TEST_REF: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_BLEND_DST: ClassVar[int]
    GL_BLEND_SRC: ClassVar[int]
    GL_BUFFER_ACCESS: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_CLIENT_ACTIVE_TEXTURE: ClassVar[int]
    GL_CLIP_PLANE0: ClassVar[int]
    GL_CLIP_PLANE1: ClassVar[int]
    GL_CLIP_PLANE2: ClassVar[int]
    GL_CLIP_PLANE3: ClassVar[int]
    GL_CLIP_PLANE4: ClassVar[int]
    GL_CLIP_PLANE5: ClassVar[int]
    GL_COLOR_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_COLOR_ARRAY_POINTER: ClassVar[int]
    GL_COLOR_ARRAY_SIZE: ClassVar[int]
    GL_COLOR_ARRAY_STRIDE: ClassVar[int]
    GL_COLOR_ARRAY_TYPE: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMBINE: ClassVar[int]
    GL_COMBINE_ALPHA: ClassVar[int]
    GL_COMBINE_RGB: ClassVar[int]
    GL_CONSTANT: ClassVar[int]
    GL_COORD_REPLACE_OES: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_COLOR: ClassVar[int]
    GL_CURRENT_NORMAL: ClassVar[int]
    GL_CURRENT_TEXTURE_COORDS: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DOT3_RGB: ClassVar[int]
    GL_DOT3_RGBA: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_GENERATE_MIPMAP: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_INTERPOLATE: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LOGIC_OP_MODE: ClassVar[int]
    GL_MATRIX_MODE: ClassVar[int]
    GL_MAX_CLIP_PLANES: ClassVar[int]
    GL_MODELVIEW_MATRIX: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_NORMAL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_NORMAL_ARRAY_POINTER: ClassVar[int]
    GL_NORMAL_ARRAY_STRIDE: ClassVar[int]
    GL_NORMAL_ARRAY_TYPE: ClassVar[int]
    GL_OPERAND0_ALPHA: ClassVar[int]
    GL_OPERAND0_RGB: ClassVar[int]
    GL_OPERAND1_ALPHA: ClassVar[int]
    GL_OPERAND1_RGB: ClassVar[int]
    GL_OPERAND2_ALPHA: ClassVar[int]
    GL_OPERAND2_RGB: ClassVar[int]
    GL_POINT_DISTANCE_ATTENUATION: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_POINTER_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_STRIDE_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_TYPE_OES: ClassVar[int]
    GL_POINT_SIZE_MAX: ClassVar[int]
    GL_POINT_SIZE_MIN: ClassVar[int]
    GL_POINT_SPRITE_OES: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_PREVIOUS: ClassVar[int]
    GL_PRIMARY_COLOR: ClassVar[int]
    GL_PROJECTION_MATRIX: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_RGB_SCALE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SHADE_MODEL: ClassVar[int]
    GL_SRC0_ALPHA: ClassVar[int]
    GL_SRC0_RGB: ClassVar[int]
    GL_SRC1_ALPHA: ClassVar[int]
    GL_SRC1_RGB: ClassVar[int]
    GL_SRC2_ALPHA: ClassVar[int]
    GL_SRC2_RGB: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_SUBTRACT: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_POINTER: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_SIZE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_STRIDE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_TYPE: ClassVar[int]
    GL_TEXTURE_MATRIX: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_VERTEX_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ARRAY_TYPE: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    GL_ADD: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALPHA_TEST: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_AMBIENT: ClassVar[int]
    GL_AMBIENT_AND_DIFFUSE: ClassVar[int]
    GL_AND: ClassVar[int]
    GL_AND_INVERTED: ClassVar[int]
    GL_AND_REVERSE: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_CLEAR: ClassVar[int]
    GL_COLOR_ARRAY: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_LOGIC_OP: ClassVar[int]
    GL_COLOR_MATERIAL: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ATTENUATION: ClassVar[int]
    GL_COPY: ClassVar[int]
    GL_COPY_INVERTED: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECAL: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DIFFUSE: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_EMISSION: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EQUIV: ClassVar[int]
    GL_EXP: ClassVar[int]
    GL_EXP2: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLAT: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FOG: ClassVar[int]
    GL_FOG_COLOR: ClassVar[int]
    GL_FOG_DENSITY: ClassVar[int]
    GL_FOG_END: ClassVar[int]
    GL_FOG_HINT: ClassVar[int]
    GL_FOG_MODE: ClassVar[int]
    GL_FOG_START: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LIGHT0: ClassVar[int]
    GL_LIGHT1: ClassVar[int]
    GL_LIGHT2: ClassVar[int]
    GL_LIGHT3: ClassVar[int]
    GL_LIGHT4: ClassVar[int]
    GL_LIGHT5: ClassVar[int]
    GL_LIGHT6: ClassVar[int]
    GL_LIGHT7: ClassVar[int]
    GL_LIGHTING: ClassVar[int]
    GL_LIGHT_MODEL_AMBIENT: ClassVar[int]
    GL_LIGHT_MODEL_TWO_SIDE: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_ATTENUATION: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_SMOOTH: ClassVar[int]
    GL_LINE_SMOOTH_HINT: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_LIGHTS: ClassVar[int]
    GL_MAX_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_MAX_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_UNITS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MODELVIEW: ClassVar[int]
    GL_MODULATE: ClassVar[int]
    GL_MULTISAMPLE: ClassVar[int]
    GL_NAND: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NOOP: ClassVar[int]
    GL_NOR: ClassVar[int]
    GL_NORMALIZE: ClassVar[int]
    GL_NORMAL_ARRAY: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OR: ClassVar[int]
    GL_OR_INVERTED: ClassVar[int]
    GL_OR_REVERSE: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_PALETTE4_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE4_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE4_RGB8_OES: ClassVar[int]
    GL_PALETTE4_RGBA4_OES: ClassVar[int]
    GL_PALETTE4_RGBA8_OES: ClassVar[int]
    GL_PALETTE8_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE8_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE8_RGB8_OES: ClassVar[int]
    GL_PALETTE8_RGBA4_OES: ClassVar[int]
    GL_PALETTE8_RGBA8_OES: ClassVar[int]
    GL_PERSPECTIVE_CORRECTION_HINT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SMOOTH: ClassVar[int]
    GL_POINT_SMOOTH_HINT: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_SMOOTH_HINT: ClassVar[int]
    GL_POSITION: ClassVar[int]
    GL_PROJECTION: ClassVar[int]
    GL_QUADRATIC_ATTENUATION: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RESCALE_NORMAL: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_ONE: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SET: ClassVar[int]
    GL_SHININESS: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SMOOTH: ClassVar[int]
    GL_SMOOTH_LINE_WIDTH_RANGE: ClassVar[int]
    GL_SMOOTH_POINT_SIZE_RANGE: ClassVar[int]
    GL_SPECULAR: ClassVar[int]
    GL_SPOT_CUTOFF: ClassVar[int]
    GL_SPOT_DIRECTION: ClassVar[int]
    GL_SPOT_EXPONENT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY: ClassVar[int]
    GL_TEXTURE_ENV: ClassVar[int]
    GL_TEXTURE_ENV_COLOR: ClassVar[int]
    GL_TEXTURE_ENV_MODE: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    GL_XOR: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def glBindBuffer(self, p0: int, p1: int) -> None: ...
    def glBufferData(self, p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    def glBufferSubData(self, p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @overload
    def glDeleteBuffers(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glDeleteBuffers(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGenBuffers(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glGenBuffers(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetBooleanv(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetBooleanv(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glGetBufferParameteriv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glGetBufferParameteriv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetFloatv(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetFloatv(self, p0: int, p1: FloatBuffer) -> None: ...
    @overload
    def glGetTexParameterfv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexParameterfv(self, p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    def glGetTexParameteriv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexParameteriv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    def glIsBuffer(self, p0: int) -> bool: ...
    def glIsEnabled(self, p0: int) -> bool: ...
    def glIsTexture(self, p0: int) -> bool: ...
    @overload
    def glTexParameterfv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glTexParameterfv(self, p0: int, p1: int, p2: FloatBuffer) -> None: ...
    def glTexParameteri(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def glTexParameteriv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glTexParameteriv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    def glColorPointer(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def glDrawElements(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def glNormalPointer(self, p0: int, p1: int, p2: int) -> None: ...
    def glTexCoordPointer(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def glVertexPointer(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def glClipPlanef(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glClipPlanef(self, p0: int, p1: FloatBuffer) -> None: ...
    @overload
    def glClipPlanex(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glClipPlanex(self, p0: int, p1: IntBuffer) -> None: ...
    def glColor4ub(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def glGetClipPlanef(self, p0: int, p1: FloatBuffer) -> None: ...
    @overload
    def glGetClipPlanef(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetClipPlanex(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glGetClipPlanex(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetFixedv(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glGetFixedv(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glGetLightfv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetLightfv(self, p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    def glGetLightxv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glGetLightxv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetMaterialfv(self, p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    def glGetMaterialfv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetMaterialxv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glGetMaterialxv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexEnviv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glGetTexEnviv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexEnvxv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexEnvxv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glGetTexParameterxv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glGetTexParameterxv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    def glPointParameterf(self, p0: int, p1: float) -> None: ...
    @overload
    def glPointParameterfv(self, p0: int, p1: Any, p2: int) -> None: ...
    @overload
    def glPointParameterfv(self, p0: int, p1: FloatBuffer) -> None: ...
    def glPointParameterx(self, p0: int, p1: int) -> None: ...
    @overload
    def glPointParameterxv(self, p0: int, p1: IntBuffer) -> None: ...
    @overload
    def glPointParameterxv(self, p0: int, p1: Any, p2: int) -> None: ...
    def glPointSizePointerOES(self, p0: int, p1: int, p2: Buffer) -> None: ...
    def glTexEnvi(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def glTexEnviv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glTexEnviv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    def glTexParameterxv(self, p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    def glTexParameterxv(self, p0: int, p1: int, p2: Any, p3: int) -> None: ...
    def glGetPointerv(self, p0: int, p1: Any) -> None: ...

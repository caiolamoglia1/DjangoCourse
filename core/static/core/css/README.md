# CSS Organization - Django Blog

Este arquivo documenta a nova estrutura organizacional do CSS do projeto Django Blog.

## Estrutura de Arquivos CSS

### Arquivo Principal
- `style.css` - Arquivo principal que importa todos os outros arquivos CSS

### Arquivos Organizados por Página/Componente

#### 1. Base Styles (`css/base.css`)
- **Conteúdo**: Estilos globais, reset, sidebar, componentes básicos
- **Inclui**:
  - Reset CSS e configurações básicas
  - Sidebar navbar com animações
  - Botões e formulários globais
  - Componentes compartilhados
  - Tipografia base
  - Layout principal (main-content)

#### 2. Home Page (`css/home.css`)
- **Conteúdo**: Estilos específicos da página inicial
- **Inclui**:
  - Hero section com animações
  - Cards de tecnologia flutuantes
  - Seção de features
  - Grid de artigos em destaque
  - Learning path com conectores
  - Call-to-action section
  - Estatísticas e badges

#### 3. Sobre Page (`css/sobre.css`)
- **Conteúdo**: Estilos específicos da página sobre
- **Inclui**:
  - Hero da página sobre
  - Cards de missão da empresa
  - Seção da equipe
  - Estatísticas de impacto
  - Informações de contato
  - Links para redes sociais

#### 4. Recursos Page (`css/recursos.css`)
- **Conteúdo**: Estilos específicos da página de recursos
- **Inclui**:
  - Hero da página recursos
  - Filtros e busca de recursos
  - Grid de recursos com categorias
  - Cards de recursos recomendados
  - Sistema de paginação
  - Estados de loading e empty

#### 5. Artigos Page (`css/artigos.css`)
- **Conteúdo**: Estilos específicos da página de artigos
- **Inclui**:
  - Hero da página artigos
  - Filtros de categoria
  - Grid de artigos com cards modernos
  - Artigo em destaque
  - Newsletter subscription
  - Meta informações dos artigos

#### 6. Contato Page (`css/contato.css`)
- **Conteúdo**: Estilos específicos da página de contato
- **Inclui**:
  - Hero da página contato
  - Formulário de contato com validação
  - Informações de contato
  - Mapa/localização
  - FAQ section
  - Redes sociais

#### 7. Cadastro Page (`css/cadastro.css`)
- **Conteúdo**: Estilos específicos da página de cadastro
- **Inclui**:
  - Formulário multi-step
  - Progress indicator
  - Floating labels
  - Validação visual
  - Upload de arquivos
  - Navegação entre etapas

#### 8. Login Page (`css/login.css`)
- **Conteúdo**: Estilos específicos da página de login
- **Inclui**:
  - Hero da página login
  - Formulário de login elegante
  - Floating labels
  - Toggle de senha
  - Social login buttons
  - Features section
  - Estados de loading

## Vantagens da Nova Estrutura

### 1. Manutenibilidade
- ✅ Cada página tem seu próprio arquivo CSS
- ✅ Fácil localização de estilos específicos
- ✅ Redução de conflitos entre estilos
- ✅ Código mais organizado e legível

### 2. Performance
- ✅ Carregamento modular (apenas o necessário)
- ✅ Cache independente por arquivo
- ✅ Possibilidade de lazy loading
- ✅ Redução do tamanho total quando necessário

### 3. Desenvolvimento
- ✅ Trabalho em equipe mais eficiente
- ✅ Merge conflicts reduzidos
- ✅ Debugging mais rápido
- ✅ Reutilização de componentes

### 4. Escalabilidade
- ✅ Fácil adição de novas páginas
- ✅ Estrutura clara e consistente
- ✅ Componentização natural
- ✅ Preparado para futura modularização

## Como Usar

### Importação Automática
O arquivo `style.css` já importa todos os arquivos automaticamente:

```css
@import url('css/base.css');
@import url('css/home.css');
@import url('css/sobre.css');
@import url('css/recursos.css');
@import url('css/artigos.css');
@import url('css/contato.css');
@import url('css/cadastro.css');
@import url('css/login.css');
```

### Nos Templates
Continue usando a referência normal:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'core/style.css' %}">
```

### Adicionando Nova Página
1. Crie o arquivo CSS na pasta `css/`
2. Adicione a importação no `style.css`
3. Siga a estrutura de comentários existente

## Estrutura de Comentários

Cada arquivo segue a mesma estrutura de comentários:

```css
/* ==========================================================================
   NOME DA PAGE - Estilos específicos da página
   ========================================================================== */

/* Seção Específica */
.classe-exemplo {
    /* propriedades */
}

/* Responsive */
@media (max-width: 768px) {
    /* ajustes mobile */
}
```

## Temas e Cores

### Paleta Principal
- **Dourado**: #ffd700 (cor primária)
- **Dourado Escuro**: #e0c200 (hover states)
- **Fundo Principal**: #181a1b
- **Fundo Secundário**: #23272b
- **Fundo Cards**: #2c3136
- **Texto Principal**: #e0e0e0
- **Texto Secundário**: #b0b0b0
- **Texto Muted**: #888

### Gradientes Padrão
```css
/* Gradiente Principal */
background: linear-gradient(135deg, #ffd700, #e0c200);

/* Gradiente de Fundo */
background: linear-gradient(135deg, #23272b, #2c3136);

/* Gradiente Hero */
background: linear-gradient(135deg, #181a1b 0%, #23272b 100%);
```

## Responsividade

Todos os arquivos seguem o padrão mobile-first com breakpoints:

```css
/* Mobile First - até 768px é padrão */

/* Tablet e Desktop */
@media (min-width: 769px) {
    /* estilos para telas maiores */
}

/* Específico Mobile */
@media (max-width: 768px) {
    /* ajustes específicos mobile */
}
```

## Animações

### Animações Globais (base.css)
- Fade in/out
- Scale transformations
- Hover effects
- Transitions padrão

### Animações Específicas
Cada página tem suas próprias animações contextuais:
- Home: floating cards, pulse effects
- Login: slide in, form validation
- Cadastro: progress animations
- Etc.

---

**Desenvolvido para o Django Blog Project**  
*Estrutura CSS Organizada e Escalável*

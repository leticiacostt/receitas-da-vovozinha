unit Forms.Main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    listar: TButton;
    Memo1: TMemo;
    procedure listarClick(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.listarClick(Sender: TObject);
var
  i: Integer;
begin
  Memo1.lines.Clear;
  for i := 0 to 10 do begin
     Memo1.Lines.Append(i.ToString);
  end;
  Memo1.Show;
end;

end.

